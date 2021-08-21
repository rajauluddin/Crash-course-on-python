file_counts = {"jpg": 10, "txt": 25, "csv": 45, "py": 20}
for extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():
    print("therre are {} files with .{} extension".format(amount,ext))

print(file_counts.keys())
print(file_counts.values())

for value in file_counts.values():
    print(value)
    