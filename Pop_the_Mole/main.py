import tkinter as tk
import threading
import random
import time
import json
import os

class PopTheMole:
    def __init__(self, root):
        self.root = root
        self.root.title("Pop The Mole 🐹🔨")

        # --- Stato del Gioco ---
        self.HighScore = 0
        if os.path.exists("data/score.json"):
            with open("data/score.json", "r") as f:
                saved_data = json.load(f)
                self.HighScore = saved_data.get("HighScore", 0)

        self.score = 0
        self.time_left = 120
        self.game_running = False
        self.active_mole = None

        # --- Difficoltà ---
        self.difficulty = "Normal"
        self.speed = 0.8

        # --- UI ---
        self.buttons = []
        self.setup_ui()

        # --- THREAD AVVIATI UNA SOLA VOLTA ---
        threading.Thread(target=self.timer_loop, daemon=True).start()
        threading.Thread(target=self.spawn_loop, daemon=True).start()

    # ---------------- UI ----------------
    def setup_ui(self):
        self.label_info = tk.Label(
            self.root,
            text="Seleziona difficoltà e premi START",
            font=("Courier", 16, "bold")
        )
        self.label_info.pack(pady=10)

        # --- Selezione difficoltà ---
        diff_frame = tk.Frame(self.root)
        diff_frame.pack(pady=5)

        tk.Label(diff_frame, text="Difficulty:").pack(side="left", padx=5)

        self.easy_btn = tk.Button(
            diff_frame, text="Easy",
            command=lambda: self.set_difficulty("Easy")
        )
        self.easy_btn.pack(side="left", padx=5)

        self.normal_btn = tk.Button(
            diff_frame, text="Normal",
            command=lambda: self.set_difficulty("Normal")
        )
        self.normal_btn.pack(side="left", padx=5)

        self.hard_btn = tk.Button(
            diff_frame, text="Hard",
            command=lambda: self.set_difficulty("Hard")
        )
        self.hard_btn.pack(side="left", padx=5)

        # --- Pulsanti ---
        self.start_button = tk.Button(
            self.root, text="START",
            font=("Arial", 14, "bold"),
            bg="lightblue",
            command=self.start_game
        )
        self.start_button.pack(pady=10)

        self.restart_button = tk.Button(
            self.root, text="RESET",
            font=("Arial", 14, "bold"),
            bg="lightcoral",
            command=self.restart_game
        )
        self.restart_button.pack(pady=5)

        # --- Griglia ---
        frame_grid = tk.Frame(self.root)
        frame_grid.pack(padx=20, pady=20)

        for i in range(9):
            btn = tk.Button(
                frame_grid,
                text="",
                width=8,
                height=4,
                font=("Arial", 12, "bold"),
                bg="bisque",
                state="disabled",
                command=lambda i=i: self.handle_click(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

    # ---------------- DIFFICOLTÀ ----------------
    def set_difficulty(self, level):
        if self.game_running:
            return

        self.difficulty = level
        self.speed = {"Easy": 1.0, "Normal": 0.8, "Hard": 0.6}[level]

        self.label_info.config(
            text=f"Difficoltà: {level} | Premi START"
        )

    # ---------------- START ----------------
    def start_game(self):
        self.game_running = True
        self.start_button.config(state="disabled")

        self.easy_btn.config(state="disabled")
        self.normal_btn.config(state="disabled")
        self.hard_btn.config(state="disabled")

        for b in self.buttons:
            b.config(state="normal")

        self.update_display()

    # ---------------- RESET ----------------
    def restart_game(self):
        self.game_running = False
        self.score = 0
        self.time_left = 120
        self.active_mole = None

        self.label_info.config(
            text="Seleziona difficoltà e premi START",
            fg="black"
        )

        self.start_button.config(state="normal")
        self.easy_btn.config(state="normal")
        self.normal_btn.config(state="normal")
        self.hard_btn.config(state="normal")

        for b in self.buttons:
            b.config(text="", bg="bisque", state="disabled")

    # ---------------- INPUT ----------------
    def handle_click(self, index):
        if not self.game_running:
            return

        if index == self.active_mole:
            self.score += 1
            self.active_mole = None
            self.buttons[index].config(text="💥", bg="orange")

            if self.score % 5 == 0 and self.speed > 0.55:
                self.speed -= 0.05
        else:
            if self.score > 0:
                self.score -= 1

        self.update_display()

    # ---------------- THREAD TALPE ----------------
    def spawn_loop(self):
        while True:
            if self.game_running:
                index = random.randint(0, 8)
                self.active_mole = index

                self.root.after(
                    0, lambda i=index: self.buttons[i].config(text="🐹", bg="lightgreen")
                )

                time.sleep(self.speed)

                self.root.after(
                    0, lambda i=index: self.buttons[i].config(text="", bg="bisque")
                )

                self.active_mole = None
                time.sleep(0.5)
            else:
                time.sleep(0.1)

    # ---------------- THREAD TIMER ----------------
    def timer_loop(self):
        while True:
            if self.game_running and self.time_left > 0:
                self.update_display()
                time.sleep(1)
                self.time_left -= 1

                if self.time_left == 0:
                    self.game_running = False
                    self.root.after(0, self.finish_game)
            else:
                time.sleep(0.1)

    # ---------------- UTILITY ----------------
    def update_display(self):
        text = (
            f"Tempo: {self.time_left}s | "
            f"Punti: {self.score} | "
            f"High Score: {self.HighScore} | "
            f"Diff: {self.difficulty}"
        )
        self.root.after(0, lambda: self.label_info.config(text=text))

    # ---------------- FINE ----------------
    def finish_game(self):
        self.save_score()

        record = self.score >= self.HighScore
        if record:
            self.HighScore = self.score

        self.label_info.config(
            text=f"GAME OVER! Score: {self.score}"
                 + ("  - NEW HIGH SCORE!" if record else ""),
            fg="red"
        )

        for b in self.buttons:
            b.config(state="disabled")

    def save_score(self):
        os.makedirs("data", exist_ok=True)
        data = {
            "score": self.score,
            "HighScore": max(self.score, self.HighScore),
            "difficulty": self.difficulty,
            "duration": 120
        }
        with open("data/score.json", "w") as f:
            json.dump(data, f, indent=4)

# ---------------- AVVIO ----------------
if __name__ == "__main__":
    root = tk.Tk()
    PopTheMole(root)
    root.mainloop()
