import streamlit

streamlit.title("Welcome sumit_dj_website")
#streamlit.header("python")
#streamlit.subheader("java")
#streamlit.code("""#for i in range(1,5,1):
    #print("your range is :",i)   """)"""

name = streamlit.text_input("Enter your name : ")
fname = streamlit.text_input("Enter your father name : ")
addr = streamlit.text_area("Enter your dil ki baat : ")
classdata = streamlit.selectbox("Enter your class : ",(1,2,3,4,5,6,7,8,9,10,11,12))

button = streamlit.button("Done")
if button:
    streamlit.markdown(f"""
    Name : {name}
    Father name : {fname}
    Address : {addr} 
    class : {classdata} """)




