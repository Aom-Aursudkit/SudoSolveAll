def CopyCodeAndGetF(x):
    clipboard = ""
    ans = []
    for i in range(len(x)):
        if x[i] == "Cut":
            if len(ans) > 0:
                clipboard = ans[len(ans)-1]
                ans.remove(ans[len(ans)-1])
        elif x[i] == "Copy":
            if len(ans) > 0:
                clipboard = ans[len(ans)-1]
        elif x[i] == "Paste":
            ans.append(clipboard)
        elif x[i] == "Delete":
            if len(ans) > 0:
                ans.remove(ans[len(ans)-1])
        else:
            ans.append(x[i])
    return ans

print(CopyCodeAndGetF(['a','Copy','b','Cut','Delete','c','d','Paste']))
print(CopyCodeAndGetF(['Copy','a','b','Paste','Delete']))
print(CopyCodeAndGetF(['Paste','a','b','c','Copy','k','k','Delete']))


