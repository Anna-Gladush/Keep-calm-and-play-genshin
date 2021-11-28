def sort_sentence(sentence):
    result_sentence = sentence.split(" ")
    result_sentence.sort(key=len)
    result_sentence = ' '.join(result_sentence).capitalize()
    return result_sentence
