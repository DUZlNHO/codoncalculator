from libretranslatepy import LibreTranslateAPI

def translation(text):
    lt = LibreTranslateAPI("https://translate.argosopentech.com/")

    translated = lt.translate(text, "en", "pt")

    return translated

if __name__ == "__main__":
    print(translation("Hello World"))