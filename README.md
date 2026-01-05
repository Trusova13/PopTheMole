# 🐹🔨 Pop the Mole

**Pop the Mole** is a reflex-based mini game developed in Python, inspired by the classic arcade game **Whack-a-Mole**.

The project was created as part of a school assignment to practice Python programming, graphical interfaces, data management and concurrent programming.

---

## 🎯 Project Objectives

The main goals of the project are:
- Develop a playable game using **Python 3**
- Create a **Graphical User Interface (GUI)** with Tkinter
- Use **threading** to manage parallel tasks
- Save and load game data using **JSON files**
- Work in a team following a structured project organization

---

## 🕹️ Gameplay Description

- The player must hit the moles as they randomly appear on the screen
- Each correct hit increases the score
- Clicking on the wrong spot decreases the score
- The game lasts **2 minutes**
- At the end of the game, the final score and the high score are saved

---

## ⚙️ Features

- Graphical interface built with **Tkinter**
- Random mole spawning
- Countdown timer
- **Three difficulty levels**:
  - Easy
  - Normal
  - Hard
- Difficulty selectable only before starting the game
- High Score saved persistently in a JSON file
- Restart functionality

---

## 🧵 Concurrent Programming

The game uses **multiple threads** to ensure smooth gameplay:
- One thread manages the **game timer**
- One thread manages the **mole spawning**

This allows the game to run without freezing the graphical interface.

---

## 💾 Data Management

Game data is saved in JSON format:
- Current score
- High Score
- Selected difficulty
- Game duration

All data is stored in the `data/score.json` file.

---

## 📁 Project Structure

#------VERSIONE IN ITALIANO----------------------------------------

# 🐹🔨 Pop the Mole

**Pop the Mole** è un mini gioco basato sui riflessi sviluppato in Python, ispirato al celebre gioco arcade **Whack-a-Mole**.

Il progetto è stato realizzato come compito scolastico per mettere in pratica la programmazione in Python, la gestione di interfacce grafiche, la gestione dei dati e la programmazione concorrente.

---

## 🎯 Obiettivi del progetto

Gli obiettivi principali del progetto sono:
- Sviluppare un gioco giocabile usando **Python 3**
- Creare un'interfaccia grafica (**GUI**) con Tkinter
- Utilizzare il **threading** per gestire attività parallele
- Salvare e caricare i dati del gioco tramite **file JSON**
- Lavorare in team seguendo una struttura di progetto chiara

---

## 🕹️ Descrizione del gioco

- Il giocatore deve colpire le talpe che appaiono casualmente sullo schermo
- Ogni colpo corretto aumenta il punteggio
- Cliccare nei posti sbagliati diminuisce il punteggio
- La partita dura **2 minuti**
- Al termine, il punteggio finale e l’High Score vengono salvati

---

## ⚙️ Funzionalità principali

- Interfaccia grafica realizzata con **Tkinter**
- Comparsa casuale delle talpe
- Timer countdown
- **Tre livelli di difficoltà**:
  - Easy
  - Normal
  - Hard
- La difficoltà può essere selezionata **solo prima dello START**
- High Score salvato in modo persistente in un file JSON
- Funzionalità di **Reset/Restart**

---

## 🧵 Programmazione concorrente

Il gioco utilizza **più thread** per garantire un'esecuzione fluida:
- Un thread gestisce il **timer della partita**
- Un thread gestisce la **comparsa delle talpe**

In questo modo il gioco rimane reattivo e la GUI non si blocca.

---

## 💾 Gestione dei dati

I dati del gioco vengono salvati in formato JSON:
- Punteggio corrente
- High Score
- Difficoltà selezionata
- Durata della partita

Tutti i dati vengono salvati nel file `data/score.json`.

---

## 📁 Struttura del progetto

