import pickle
import nltk
import TranslaterLogic
import streamlit as st

translatorPic = open("trigramTrans.pickle", "rb")
translator = pickle.load(translatorPic)


def triGramTranslate(sentence):
    sentence_romanized=sentence.split(" ")
    translation = ""
    translated = translator.tag(nltk.word_tokenize(sentence.lower()))
    #print(translated)
    i=-1
    for word, trans in translated:
        i+=1
        if trans in ('NNN'):
            translation = translation + str(TranslaterLogic.convertText(str(sentence_romanized[i])) + " ")
        else:
            translation = translation + str(trans + " ")
    return translation
def main():
   
# Your existing code for the translator 
    st.set_page_config(page_title="Tranliterator", page_icon=":robot_face:")
    st.header("Swabhasha Translator")
    st.subheader("Romanized Sinhala to Sinhala Transliterator")

    # Assuming you have the triGramTranslate function defined 

    def text_input_callback():
        translated_text = triGramTranslate(st.session_state.input_text)
        st.session_state.output_text = translated_text
        
        

    # Initialize session state variables if they don't exist
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""
    if "output_text" not in st.session_state:
        st.session_state.output_text = ""

    # Text input/output fields
    textinput_text = st.text_input("Enter the input", key="input_text", on_change=text_input_callback)
    textoutput_text = st.text_input("Sinhala Text", value=st.session_state.output_text) 
    

     


if __name__ == '__main__':
    main()

