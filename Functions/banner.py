def banner_text(text, screen_width):
    if len(text) > screen_width - 4:
        # print("EEK!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
        raise ValueError("String {0} is larger then specified width{1}".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*", 66)
banner_text("Always look on the bright side of life...", 66)
banner_text("If life seems jolly rotten,", 66)
banner_text("There's something you've forgotten!", 66)
banner_text("And that's to laugh and smile and dance and sing,", 66)
banner_text(" ", 66)
banner_text("When you're feeling in the dumps,", 66)
banner_text("Don't be silly chumps,", 66)
banner_text("Just purse your lips and whistle - that's the thing!", 66)
banner_text("And... always look on the bright side of life...", 66)
banner_text("*", 66)

result = banner_text("Nothing is returned", 66)
print(result)

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort())
