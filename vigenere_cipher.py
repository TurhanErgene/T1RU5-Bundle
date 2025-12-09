cipher = "knvhrmftxkflrziughvytdpegxserrviluvskkrhqszzeznscgyqphvjjubmgnsebsknilanvxqrbnflqdeskniiyixnxwvmvcevfemkrzrebyeqqtykmqftiaqhatngwvjikilhqtf"

# Longer ciphertext for actual cryptanalysis
cipher2 = "knvhrmftxkflrziughvytdpegxserrviluvskkrhqszzeznscgyqphvjjubmgnsebsknilanvxqrbnflqdeskniiyixnxwvmvcevfemkrzrebyeqqtykmqftiaqhatngwvjikilhqtflyoypfciubncejliedorxgejhiibrvorwrrtktwvoeymphlkgrhbujrcdpllyxheowieprrrvsgfwryvhyeryiggojgmocajzvdzajuxkntzzgrhluhisuokukunpykhieodgpofiukwwuewovvgidgkhffiuqwrnknsxfaejolyodkxhesrceborfakkgtfgldytknidptzbmwvejujdyldgrnvnuurdoicrmratvriyvszurvprvkrvghvxidcpvgvhqakorbserzyurlvywfllzthhegiualagigtlqlpyifbnuhcvrcftheltykxlzezzldqdfafordzzwvvzvtsraetuyoqpikxhadrtcobnxkvwuakxepnwryeqntlxeobbakgwvtjhsglwryefllzthhesfmirzekxmfnlcethefvixwuakoxpvgyzldieskiqguitigbnrrewueftizvtyiiqgeiyjlstpqmobmvziufaggvwghvzarrnuyaheekciqgyboprzekkvvnciuwvsrfsegvskgrfrwykrwueikadfnfyiqfeflwfnlvxepnlfuohqacssvgcfsmfnlceplxertsuqiegvbqodkwwvcsumorrigqdtrvcyqgicoxivlckhwuejivhrnzzwvhrwgghjajghxyluxeetrreevpocuvorsjgwwuedusqnnuispclvzioldvbslqowseuxiemwhkcvvxdgoektrvnkneoswreeobnxzlhpycorgrrkniurwryenvlfsiwrrnohhftrorresdkeunszlwrzeknmqthrjsqpeyoxdadjvpdgtvxigngvyejbtykvhjajtsvvgezldgtykmpcatzldqdftiwuejrmjutvyxgnmrmiwbrrsevfpztrlagngpofblzxkvsdgvnuauvvrqutkhwuejrmjutwryfgurzmraiehvlthktivftygxkndckhwbskkrwbnjjmvpomkvbghvoqdtejlvrztykswueiieprrryegqeutswuiemrhjhfciyrrkniweaakgwbrzkwwuezxtrqskxefrdknvrhgyxepnsdorxgexxeyvtrzmraaclmhydxgzhbnvuxkrrmoxdypvoghbfztjremrzmratykqdfsflxkrcprmqqeioxznswgvwbocokkgtfhidfocohebdpzsqbbfjcvtrvgxvhrgxmvrikcevplvgvwuakxepnmlyxerhfrprjtykpragyuthqffxpragwkeurdvtgrhnkkvkndtuqhntcgwwzaeqmqqwryeebukzsurcvozhghvlmuftmowlgoilvrztykwwnrj"


def kasiski(text):
    """
    Visual helper: prints the ciphertext in a diagonal pattern and counts
    column matches between the original and an offset version.
    This can give a rough visual hint of possible key lengths but is
    not a full Kasiski examination implementation.
    """
    for i in range(len(text), 1, -1):
        # Number of spaces to indent the substring
        spc = len(text) - i
        print(" " * spc, end="")

        # Substring starting at index 0 of length i
        substring = text[:i]
        print(substring, end="")

        # Count how many characters match when compared with the
        # original text shifted to the right by 'spc' positions
        match_count = 0
        for j in range(len(substring)):
            if substring[j] == text[spc + j]:
                match_count += 1

        print(f" {match_count}")


kasiski(cipher)


from collections import Counter


def frequency_analysis(ciphertext):
    """
    Count letter frequencies in 'ciphertext' and return a dictionary
    mapping each letter to its percentage occurrence.
    Non-alphabetic characters are ignored.
    """
    counts = Counter(char.lower() for char in ciphertext if char.isalpha())
    total_letters = sum(counts.values())

    frequency_percentage = {
        char: (count / total_letters) * 100 for char, count in counts.items()
    }
    return frequency_percentage


freq_analysis = frequency_analysis(cipher2)
print("\n=== Global Letter Frequencies ===")
for char, freq in sorted(freq_analysis.items()):
    print(f"{char}: {freq:.2f}%")


# English language letter frequencies (in percentage)
english_freq = {
    'a': 8.17, 'b': 1.29, 'c': 2.78, 'd': 4.25, 'e': 12.70,
    'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 7.00, 'j': 0.15,
    'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
    'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
    'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97,
    'z': 0.07
}

# Note: this section treats the ciphertext as if it were encrypted with a
# single Caesar shift and tries all 26 shifts, comparing the resulting
# distribution with English. This is only directly useful if the key length
# is 1 (pure Caesar), but it's still instructive.

print("\n=== Shift Analysis on Full Cipher (Caesar-style) ===")
best_shift = 0
best_score = 0

for shift in range(26):
    # Shift ciphertext frequencies BACKWARD by 'shift' positions.
    # For a true Caesar cipher with shift k, the best correlation occurs
    # when 'shift' equals k.
    shifted_freq = {}
    for char, freq in freq_analysis.items():
        shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        shifted_freq[shifted_char] = shifted_freq.get(shifted_char, 0) + freq

    # Correlation score with English frequencies
    score = 0
    for char in english_freq:
        observed = shifted_freq.get(char, 0)      # frequency after shift
        expected = english_freq[char]            # English frequency
        score += (observed * expected) / 100

    print(f"Shift {shift:2d}: {score:.4f}")

    if score > best_score:
        best_score = score
        best_shift = shift

print(f"\nBest global Caesar shift (for key length 1): {best_shift} with score {best_score:.4f}")


# For this specific ciphertext, the actual Vigenere key length is 6.
# Once the key length is known, we split the ciphertext into 6 subsets:
# each subset contains characters encrypted with the same key letter.

key_length = 6  # for this cipher, the true key length

print("\n=== Splitting Ciphertext Into Subsets By Key Position ===")
subsets = [[] for _ in range(key_length)]
for i, char in enumerate(cipher2):
    position = i % key_length
    subsets[position].append(char)

subset_strings = [''.join(subset) for subset in subsets]

for i, subset in enumerate(subset_strings):
    print(f"Position {i}: {subset[:80]}...")


print("\n=== Frequency Analysis For Each Key Position ===")
subset_freq_analysis = []
for i, subset in enumerate(subset_strings):
    print(f"\nPosition {i}:")
    freq = frequency_analysis(subset)
    subset_freq_analysis.append(freq)
    for char, freq_val in sorted(freq.items()):
        print(f"  {char}: {freq_val:.2f}%")


# Now, for each subset, we try all 26 shifts to find which shift makes
# the subset's distribution look most like English. That shift corresponds
# to the key letter for that position.

print("\n=== Shift Correlation For Each Key Position ===")
key = [None] * key_length

for pos in range(key_length):
    print(f"\nPosition {pos}:")
    best_shift_pos = 0
    best_score_pos = 0

    for shift in range(26):
        # Shift subset frequencies BACKWARD by 'shift' positions.
        # This is the critical fix: we subtract 'shift' instead of adding it.
        shifted_freq = {}
        for char, freq in subset_freq_analysis[pos].items():
            shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            shifted_freq[shifted_char] = shifted_freq.get(shifted_char, 0) + freq

        # Correlation score with English frequencies
        score = 0
        for char in english_freq:
            observed = shifted_freq.get(char, 0)
            expected = english_freq[char]
            score += (observed * expected) / 100

        print(f"  Shift {shift:2d}: {score:.4f}")

        if score > best_score_pos:
            best_score_pos = score
            best_shift_pos = shift

    # The best shift index is the key letter index: 0 -> 'a', 1 -> 'b', etc.
    key_letter = chr(best_shift_pos + ord('a'))
    key[pos] = key_letter
    print(f"  Best shift: {best_shift_pos} -> key letter: '{key_letter}'")

print("\n=== Final Key ===")
final_key = ''.join(key)
print(f"Key: {final_key}")


# Optional: Vigenere decryption using the recovered key.
def vigenere_decrypt(ciphertext, key):
    """
    Decrypt 'ciphertext' using Vigenere with the given 'key'.
    Non-alphabetic characters are copied unchanged.
    """
    plaintext = []
    key = key.lower()
    key_len = len(key)

    j = 0  # index in key
    for char in ciphertext:
        if char.isalpha():
            offset = ord('a')
            k = ord(key[j % key_len]) - offset
            p = (ord(char.lower()) - offset - k) % 26 + offset
            plaintext.append(chr(p))
            j += 1
        else:
            plaintext.append(char)

    return ''.join(plaintext)


print("\n=== Decrypted (first 300 chars) ===")
print(vigenere_decrypt(cipher2, final_key)[:300])
