# -*- coding: utf-8 -*-


class Formatter:
    def frame(text, char):
        longest = 0
        for word in text:
            if len(word) > longest:
                longest = len(word)
        result_frame = char * (longest + 4)
        for i in range(len(text)):
            result_fram = result_frame + '\n' + (char + ' ' + text[i] + (' ' * (longest + 1 - (len(text[i]))) + char))
        result_frame = result_frame + '\n' + char * (longest + 4)
        return result_frame

    def format_to_do(index, todo):
        if type(todo) not dict:
            raise Exception('Second param must be a dict')
        else:
            items = len(todo)
