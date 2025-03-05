import streamlit as st

def calculator(num1,num2,opr):

    if opr=="+":
       return num1+num2
    elif opr=="-":
        return num1-num2
    elif opr=="*":
        return num1*num2
    else:
        if num2!=0:
         return num1/num2
        else:
           return ("zero division not allowed")
        
def main():
    st.title("Welcome to my calculator")
    number1=st.number_input("enter the number", format="%2f")
    operator=st.selectbox("select operator", ["+","-","*","/"])
    number2=st.number_input("enter the number1", format="%2f")
    result=calculator(number1,number2,operator)
    if st.button("cal"):
       st.success(result)
        
if __name__=="__main__" :
   main()