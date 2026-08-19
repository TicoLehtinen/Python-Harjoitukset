import random
koodi = [random.randint(0, 9) for _ in range(3)]
print("sun kolminumeroinen koodi on:", ''.join(map(str, koodi)))