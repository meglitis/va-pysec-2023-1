forbidden_words = {'error', 'fail', 'warning'}

message = 'this error contains some failures and warnings, please correct all failed errorlements and warninged failures.'

forbidden_word_count = 0

for word in forbidden_words:
    forbidden_word_count += message.count(word)

print("There are " + str(forbidden_word_count) + " forbidden words")
