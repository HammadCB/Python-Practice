p1 ="Make a lot of Money"
p2 ="Buy now"
p3 ="Subscribe This"
p4 ="Click This"

message =input("Enter your comment")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is Spam")
else:
    print("This comment is not a spam")