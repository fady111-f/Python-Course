"""
📊 Text Analyzer
================
Videos 11-15: string methods, indexing, slicing

Analyzes any text input and provides detailed statistics
using string methods learned in Week 02.
"""

# ===== Header =====
print()
print("=" * 55)
print("  📊  PYTHON TEXT ANALYZER  📊")
print("  Using String Methods, Indexing & Slicing")
print("=" * 55)
print()

# ===== Get Input =====
print("Enter the text you want to analyze.")
print("(Type your text and press Enter)\n")
text = input("📝 Your text: ")

# ===== Guard against empty input =====
if len(text) == 0:
    print("\n⚠️  You entered empty text! Using a sample instead.\n")
    text = "Python is an Amazing programming language. Python is easy to learn!"

print()
print("=" * 55)
print("  📈  ANALYSIS RESULTS")
print("=" * 55)

# ===== 1. Basic Statistics =====
print("\n🔢 BASIC STATISTICS")
print("-" * 40)

total_chars = len(text)
chars_no_spaces = len(text.replace(" ", ""))
word_list = text.split()
word_count = len(word_list)
sentence_count = text.count(".") + text.count("!") + text.count("?")
if sentence_count == 0:
    sentence_count = 1

print("  Total characters    : " + str(total_chars))
print("  Characters (no space): " + str(chars_no_spaces))
print("  Word count          : " + str(word_count))
print("  Sentence count      : " + str(sentence_count))
print("  Average word length : " + str(round(chars_no_spaces / max(word_count, 1), 1)))

# ===== 2. Case Analysis =====
print("\n🔠 CASE ANALYSIS")
print("-" * 40)

upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0
special_count = 0

for char in text:
    if char.isupper():
        upper_count = upper_count + 1
    elif char.islower():
        lower_count = lower_count + 1
    elif char.isdigit():
        digit_count = digit_count + 1
    elif char.isspace():
        space_count = space_count + 1
    else:
        special_count = special_count + 1

print("  Uppercase letters   : " + str(upper_count))
print("  Lowercase letters   : " + str(lower_count))
print("  Digits              : " + str(digit_count))
print("  Spaces              : " + str(space_count))
print("  Special characters  : " + str(special_count))

# ===== 3. String Method Transformations =====
print("\n🔄 CASE TRANSFORMATIONS")
print("-" * 40)
print("  UPPER     : " + text.upper())
print("  lower     : " + text.lower())
print("  Title Case: " + text.title())
print("  Swap Case : " + text.swapcase())

# ===== 4. Slicing Showcase =====
print("\n✂️  SLICING SHOWCASE")
print("-" * 40)
print("  First 10 chars  : \"" + text[:10] + "\"")
print("  Last 10 chars   : \"" + text[-10:] + "\"")
print("  Reversed         : \"" + text[::-1] + "\"")
print("  Every 2nd char   : \"" + text[::2] + "\"")
if len(text) > 20:
    print("  Middle section   : \"" + text[5:15] + "\"")

# ===== 5. Search & Find =====
print("\n🔍 SEARCH & FIND")
print("-" * 40)

search_term = input("\n  Enter a word to search for: ")

if search_term:
    occurrences = text.lower().count(search_term.lower())
    position = text.lower().find(search_term.lower())

    print("  Occurrences of \"" + search_term + "\": " + str(occurrences))

    if position != -1:
        print("  First found at index: " + str(position))
    else:
        print("  ❌ Not found in the text")

    print("  Starts with \"" + search_term + "\": " + str(text.lower().startswith(search_term.lower())))
    print("  Ends with \"" + search_term + "\"  : " + str(text.lower().endswith(search_term.lower())))

# ===== 6. Character Frequency =====
print("\n📊 TOP CHARACTER FREQUENCIES")
print("-" * 40)

# Count each unique character (case-insensitive, skip spaces)
checked = ""
freq_list = []
for char in text.lower():
    if char != " " and char not in checked:
        count = text.lower().count(char)
        freq_list.append(char + ":" + str(count))
        checked = checked + char

# Sort by count (simple bubble sort since we haven't learned sorted() yet)
freq_pairs = []
for item in freq_list:
    parts = item.split(":")
    freq_pairs.append((parts[0], int(parts[1])))

# Simple sort
for i in range(len(freq_pairs)):
    for j in range(i + 1, len(freq_pairs)):
        if freq_pairs[j][1] > freq_pairs[i][1]:
            temp = freq_pairs[i]
            freq_pairs[i] = freq_pairs[j]
            freq_pairs[j] = temp

# Show top 10
top = 10
if len(freq_pairs) < top:
    top = len(freq_pairs)

for i in range(top):
    char = freq_pairs[i][0]
    count = freq_pairs[i][1]
    bar = "█" * count
    display_char = char
    if char == "\n":
        display_char = "\\n"
    elif char == "\t":
        display_char = "\\t"
    print("  '" + display_char + "' : " + bar + " (" + str(count) + ")")

# ===== 7. Word Analysis =====
print("\n📝 WORD ANALYSIS")
print("-" * 40)

if word_count > 0:
    longest = word_list[0]
    shortest = word_list[0]
    for word in word_list:
        if len(word) > len(longest):
            longest = word
        if len(word) < len(shortest):
            shortest = word

    print("  Longest word  : \"" + longest + "\" (" + str(len(longest)) + " chars)")
    print("  Shortest word : \"" + shortest + "\" (" + str(len(shortest)) + " chars)")
    print("  First word    : \"" + word_list[0] + "\"")
    print("  Last word     : \"" + word_list[-1] + "\"")

# ===== Footer =====
print()
print("=" * 55)
print("  ✅  Analysis complete!")
print("=" * 55)
print()
