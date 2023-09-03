# seccrypt

    WARNING - BE CAREFUL, I HAVEN'T MADE A DECRYPTOR YET


 <h1>File Encryption with Python</h1>

   <p>This Python script allows you to encrypt files in the current directory and its subdirectories using the Fernet encryption method from the <code>cryptography</code> library.</p>

   <h2>Usage</h2>

   <ol>
        <li>Clone the repository or download the script.</li>
        <li>Run the script using your Python interpreter.</li>
        <pre><code>python seccrypt.py</code></pre>
        <li>You will be prompted to enter an encryption password. This password is used to generate a key for encryption.</li>
        <pre><code>Enter the encryption password:</code></pre>
        <p><strong>Note:</strong> The password will not be displayed as you type it for security reasons.</p>
        <li>The script will then encrypt all files in the current directory and its subdirectories using the provided password.</li>
        <pre><code>Encrypted: /path/to/file1.txt</code></pre>
        <pre><code>Encrypted: /path/to/file2.jpg</code></pre>
        <li>Once the encryption is complete, you will see the following message:</li>
        <pre><code>Encryption complete.</code></pre>
    </ol>

  <h2>Important Notes</h2>

  <ul>
        <li>Make sure to keep your encryption password safe. You will need it to decrypt the files.</li>
        <li>This script overwrites the original files with the encrypted versions. Make sure to have backups of your files if needed.</li>
    </ul>

  <h2>Dependencies</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>cryptography</code> library</li>
    </ul>

   <p>You can install the <code>cryptography</code> library using <code>pip</code>:</p>

  <pre><code>pip install cryptography</code></pre>

