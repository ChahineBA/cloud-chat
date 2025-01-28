import streamlit as st
from prompts import agent_executor
from langchain_core.messages import HumanMessage
st.title("DepMate")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner('Wait for it...'):
        config = {"configurable": {"thread_id": "abc123"}}
        response = agent_executor.invoke({"messages": [HumanMessage(content=prompt)]},config)
        result = response['messages'][-1].content
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(result)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": result})

