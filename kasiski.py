cipher = "knvhrmftxkflrziughvytdpegxserrviluvskkrhqszzeznscgyqphvjjubmgnsebsknilanvxqrbnflqdeskniiyixnxwvmvcevfemkrzrebyeqqtykmqftiaqhatngwvjikilhqtflyoypfciubncejliedorxgejhiibrvorwrrtktwvoeymphlkgrhbujrcdpllyxheowieprrrvsgfwryvhyeryiggojgmocajzvdzajuxkntzzgrhluhisuokukunpykhieodgpofiukwwuewovvgidgkhffiuqwrnknsxfaejolyodkxhesrceborfakkgtfgldytknidptzbmwvejujdyldgrnvnuurdoicrmratvriyvszurvprvkrvghvxidcpvgvhqakorbserzyurlvywfllzthhegiualagigtlqlpyifbnuhcvrcftheltykxlzezzldqdfafordzzwvvzvtsraetuyoqpikxhadrtcobnxkvwuakxepnwryeqntlxeobbakgwvtjhsglwryefllzthhesfmirzekxmfnlcethefvixwuakoxpvgyzldieskiqguitigbnrrewueftizvtyiiqgeiyjlstpqmobmvziufaggvwghvzarrnuyaheekciqgyboprzekkvvnciuwvsrfsegvskgrfrwykrwueikadfnfyiqfeflwfnlvxepnlfuohqacssvgcfsmfnlceplxertsuqiegvbqodkwwvcsumorrigqdtrvcyqgicoxivlckhwuejivhrnzzwvhrwgghjajghxyluxeetrreevpocuvorsjgwwuedusqnnuispclvzioldvbslqowseuxiemwhkcvvxdgoektrvnkneoswreeobnxzlhpycorgrrkniurwryenvlfsiwrrnohhftrorresdkeunszlwrzeknmqthrjsqpeyoxdadjvpdgtvxigngvyejbtykvhjajtsvvgezldgtykmpcatzldqdftiwuejrmjutvyxgnmrmiwbrrsevfpztrlagngpofblzxkvsdgvnuauvvrqutkhwuejrmjutwryfgurzmraiehvlthktivftygxkndckhwbskkrwbnjjmvpomkvbghvoqdtejlvrztykswueiieprrryegqeutswuiemrhjhfciyrrkniweaakgwbrzkwwuezxtrqskxefrdknvrhgyxepnsdorxgexxeyvtrzmraaclmhydxgzhbnvuxkrrmoxdypvoghbfztjremrzmratykqdfsflxkrcprmqqeioxznswgvwbocokkgtfhidfocohebdpzsqbbfjcvtrvgxvhrgxmvrikcevplvgvwuakxepnmlyxerhfrprjtykpragyuthqffxpragwkeurdvtgrhnkkvkndtuqhntcgwwzaeqmqqwryeebukzsurcvozhghvlmuftmowlgoilvrztykwwnrj"


def kasiski(str):
    match_counts = {}
    
    for i in range(len(str), 1, -1):
        # Print leading spaces
        spc = len(str) - i
        print(" " * spc, end="")
        # Print the remaining characters from position i
        substring = str[:i]
        print(substring, end="")
        
        # Count matches: compare characters in the substring with original cipher at the same column positions
        match_count = 0
        for j in range(len(substring)):
            if substring[j] == str[spc + j]:
                match_count += 1
        
        print(f" {match_count}")
        
        # Track the frequency of each match count
        if match_count not in match_counts:
            match_counts[match_count] = 0
        match_counts[match_count] += 1
    
    # Print the summary
    print("\nMatch Frequency:")
    for count in sorted(match_counts.keys()):
        print(f"{count}: {match_counts[count]}")


kasiski(cipher)    
