
import google.generativeai as genai
genai.configure(api_key="AIzaSyCt2tPnwfAQnANE_7t67UmKrmMLiRTd2uc")
model = genai.GenerativeModel('gemini-pro')


def geminiai(mesaj):
    response = model.generate_content(str(mesaj))
    with open("output.txt", "w", encoding="UTF-8") as f:
        for chunk in response:
            f.write(chunk.text) 
    return 1

def haberler():
    response = model.generate_content("günün sabah haberleri")
    return response
if __name__ == "__main__":
    mesaj = input("Soru sor")
    response = model.generate_content(mesaj)
    for chunk in response:
            print(chunk.text)












