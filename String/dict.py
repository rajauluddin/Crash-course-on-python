file_counts = {"jpg":10, "py":15, "gif": 20}
print(type(file_counts))
print(file_counts)
print(file_counts["py"])
print("jpg" in file_counts)
file_counts["gif"] =40
print(file_counts)
del file_counts["jpg"] 
print(file_counts)

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"]=39  # Epilogue starts on page 39
toc["Chapter 3"]=24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?