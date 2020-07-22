import re
#userဆီကနေ စာသားကိုအရင်တောင်း
st=str(input("Enter a String-"))

#ကိုယ်ဖျက်ချင်တဲ့ characterတွေကိုအရင် ပုံစံလုပ်ပေး
deletchar="!#"

#patternဆောက်မယ်
pattern="["+deletchar+"]"

#re.sub(pattern,ကိုယ်ထည့်ချင်တဲ့ char,string)ကိုအသုံးပြူပီးလုပ်မယ်
print(re.sub(pattern,"",st))

