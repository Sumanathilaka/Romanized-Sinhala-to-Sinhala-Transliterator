from flask import Flask, render_template, request, jsonify
import translator_fun

app = Flask(__name__)

# Global lists to hold words and translated text
list_of_words = []
list_of_sinhala = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on_space', methods=['POST'])
def on_space():
    text = request.form.get('text')
    global list_of_words, list_of_sinhala

    if text:
        words = text.split()
        list_of_sinhala.clear()

        # All words except the last one
        result = ' '.join(words[:-1])
        list_of_sinhala.append(result)

        # Handle the last word
        last_word = words[-1]
        list_of_words.append(last_word)

        translated_word = translator_fun.triGramTranslate(last_word)
        list_of_sinhala.append(translated_word)

    concatenated_string = " ".join(list_of_sinhala) + " "
    return jsonify({"translated_text": concatenated_string})

@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    clicked_word = list_of_words[-1]

    if clicked_word:
        suggestions = translator_fun.translate(clicked_word)
        return jsonify({"suggestions": suggestions})

    return jsonify({"suggestions": []})

@app.route('/replace_word', methods=['POST'])
def replace_word():
    suggestion = request.form.get('suggestion')

    if suggestion == "delete":
        if list_of_sinhala and list_of_words:
            list_of_sinhala.pop()
            list_of_words.pop()
    else:
        list_of_sinhala[-1] = suggestion

    concatenated_string = " ".join(list_of_sinhala) + " "
    return jsonify({"translated_text": concatenated_string})

if __name__ == '__main__':
    app.run(debug=True)
