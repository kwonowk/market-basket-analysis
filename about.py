import streamlit as st

with open ("README.md", 'r') as f:
    lines = f.readlines()

print(lines)
lines = ['\n\n' if e == '<br>\n' else e for e in lines ]
lines = [e.replace('##', '@####').replace('\n','\n\n') if e.startswith('##') else e for e in lines]
print(lines)

lines = ' '.join(lines).split("@")
print(lines)
lines = lines[:-1]
print(lines)

for idx, e in enumerate(lines):

    st.markdown(e)
    st.write("")
    st.write("")
