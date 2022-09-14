# ICONIC HASHING ALGORITHM MODULE

## USAGE

1. Download the branch as a zip file or clone it.
2. Move the hash.py file to your python file directory
3. Import IHA by adding following lines into your python file
```
import IHA
```
4. Use the following commands

### To hash a string

`IHA.encode("string")`

### To generate Key 1

`IHA.key_gen1("Yourciphertext")`


### To generate Key 2

`IHA.key_gen2("Yourciphertext")`


### To generate Key 3

`IHA.key_gen3("Yourciphertext")`

### For padding a cipher text

`IHA.padding("cipher text")`

### To format(resize) a Hash

`IHA.format("hash")`

### To hash a padded String

`IHA.hash("key1", "key2", "key3")`

Please Reffer the documentation of IHA to know more about keys, padding, encoding, formating and hashing
