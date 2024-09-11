import sqlite3
import random

# Funzione per creare e popolare il database
def create_and_populate_db():
    conn = sqlite3.connect('path_to_your_database.db')  # Sostituisci con il percorso al tuo database
    cursor = conn.cursor()
    
    # Crea la tabella se non esiste già
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT,
            content TEXT
        )
    ''')
    
    # Popola il database con alcuni dati di esempio
    cursor.execute('''
        INSERT INTO messages (author, content) VALUES
        ('User1', 'Hello, world!'),
        ('User2', 'This is a test message.'),
        ('User3', 'Another random message.')
    ''')
    
    conn.commit()
    conn.close()
    print("Database creato e popolato.")

# Funzione per salvare un messaggio nel database
def save_message(author, content):
    conn = sqlite3.connect('path_to_your_database.db')  # Sostituisci con il percorso al tuo database
    cursor = conn.cursor()
    
    # Crea la tabella se non esiste già
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT,
            content TEXT
        )
    ''')
    
    # Inserisci il messaggio nella tabella
    cursor.execute('''
        INSERT INTO messages (author, content) VALUES (?, ?)
    ''', (author, content))
    
    conn.commit()
    conn.close()
    print(f"Message saved: {author}: {content}")

# Funzione per ottenere un messaggio casuale dal database
def get_random_message():
    conn = sqlite3.connect('path_to_your_database.db')  # Sostituisci con il percorso al tuo database
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM messages')
    total_messages = cursor.fetchone()[0]
    
    if total_messages == 0:
        conn.close()
        print("No messages in database.")
        return None
    
    random_index = random.randint(1, total_messages)
    cursor.execute('SELECT content FROM messages WHERE id = ?', (random_index,))
    message = cursor.fetchone()
    
    conn.close()
    
    if message:
        print(f"Random message retrieved: {message[0]}")
        return message[0]
    else:
        print("No message found.")
        return None

# Chiamata alla funzione per creare e popolare il database (solo per la prima volta)
# create_and_populate_db()  # Decommenta questa linea solo se stai creando il database per la prima volta
