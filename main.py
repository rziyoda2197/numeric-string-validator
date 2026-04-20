def tekshir(string):
    return string.isdigit()

print(tekshir("12345"))  # True
print(tekshir("abcde"))  # False
print(tekshir("123abc"))  # False
print(tekshir(""))  # False
```

```python
def tekshir(string):
    return string == string.isdigit()

print(tekshir("12345"))  # True
print(tekshir("abcde"))  # False
print(tekshir("123abc"))  # False
print(tekshir(""))  # False
