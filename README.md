# Wireshark Workshop

Mini workshop for a CyberAI club meeting. All keys and secrets in this repository are only used for this and have no use outside of this mini workshop.

## Solution

1. Open `capture.pcap` in Wireshark
2. Find the `debug.html` file from an HTTP request
3. Find the `riddle.txt` file from another HTTP request
4. Extract the RSA secret key from the `debug.html` file and save just the key to a separate file. Make sure the full key is saved, including the begin and end lines.||
5. In Wireshark open Edit > Preferences > Protocols > TLS and select "Edit" for the "RSA keys list"
6. Add a new entry with IP set to `127.0.0.1`, Port set to `4443`, Protocol to `http`, and select the key file saved in step 4 as the Key file. Select Ok to finish the entry addition.
7. Select Apply and then Ok to finish adding the RSA key.
8. Hit CTRL+R to reload the PCAP file to reveal the GET request for the `secret.zip` file (captures with ID 34 & 36)
9. Open File > Export Objects > HTTP and then select packet 36 with filename `secret.zip`.  Click the Save button and then save to a file on your file system.
10. In a terminal, with `<zipfile>` being the path to the `secret.zip` file (or `cd` into the directory containing it and just use the file name you saved it as) use `zip2john <zipfile> > hash.txt` to get a hash of the password.
11. Consult the riddle to determine that we need to use John the Ripper with the rockyou wordlist to crack the password.
12. Use the command `cd /usr/share/wordlists && sudo gunzip rockyou.txt.gz` to unzip the rockyou wordlist.
13. Use `cd` to get back to your previous directory where the `hash.txt` file is located.
14. Use `john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt` to run the password cracker.
15. When it finishes, use `john --show hash.txt` to display the results.
16. Use the cracked password to unzip the zip file and get the flag.

