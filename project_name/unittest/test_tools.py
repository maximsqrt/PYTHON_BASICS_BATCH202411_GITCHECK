# unittest/test_tools.py
import unittest
import sys
import os



### Modul `os`

""" Das `os`-Modul bietet eine Schnittstelle zu Betriebssystemfunktionen und ermöglicht es Python-Programmen, mit dem Betriebssystem zu interagieren.

- **os.path**: Eine Untermodul von `os`, das Funktionen zur Manipulation von Pfadnamen bereitstellt.
  - `os.path.join()`: Verbindet einen oder mehrere Pfadteile intelligent miteinander.
  - `os.path.abspath()`: Gibt den absoluten Pfad zurück.
  - `os.path.dirname()`: Gibt das Verzeichnis des Pfades zurück.
  - `os.path.exists()`: Überprüft, ob ein Pfad existiert.
  
- **os.environ**: Ein von Wörterbüchern abgeleitetes Objekt, das die Benutzerumgebung darstellt.
  - `os.environ.get()`: Greift sicher auf Umgebungsvariablen zu.

- **os.system()**: Führt den Befehl in einer Unter-Shell aus.

- **os.walk()**: Generiert die Dateinamen in einem Verzeichnisbaum, indem es den Baum entlanggeht (top-down oder bottom-up).

- **os.mkdir() / os.makedirs()**: Erstellt ein Verzeichnis bzw. rekursiv Verzeichnisse.

### Modul `sys`

- **sys.argv**: Eine Liste von Kommandozeilenargumenten, die an ein Python-Skript übergeben wurden.

- **sys.path**: Eine Liste von Strings, die die Suchpfade für Module angibt. Wird häufig modifiziert, um Python-Laufzeiten zusätzliche Orte anzugeben, an denen nach Modulen gesucht werden soll.

- **sys.exit()**: Ermöglicht es dem Skript, die Python-Laufzeit sauber zu beenden.

- **sys.stdin / sys.stdout / sys.stderr**: Dateiobjekte, die für die Standardeingabe, Standardausgabe und Standardfehlerausgabe verwendet werden.

- **sys.modules**: Ein Wörterbuch, das die Module darstellt, die derzeit geladen sind. Ermöglicht Zugriff auf alle Module, die aktuell vom Python-Interpreter geladen wurden.

 """

# Füge das Wurzelverzeichnis des Projekts zum Python-Suchpfad hinzu
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from lib.tools import add_numbers, multiply_numbers

class TestTools(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(4, 2), 8)

if __name__ == '__main__':
    unittest.main()
