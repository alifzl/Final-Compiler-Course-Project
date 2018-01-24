# Compute column.
# input is the input text string
# token is a token instance
def find_column(input, token):
    # when carriage return is detected, reset the counting...
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        # Not found
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    # returning the pure position of token in it's expression
    return column