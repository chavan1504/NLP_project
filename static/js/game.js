class HauntedMansionFlaskGame {
    constructor() {
        this.output = document.getElementById('gameOutput');
        this.input = document.getElementById('userInput');
        this.submitBtn = document.getElementById('submitBtn');
        this.inputSection = document.getElementById('inputSection');
        
        this.setupEventListeners();
        this.startGame();
    }

    setupEventListeners() {
        this.submitBtn.addEventListener('click', () => this.handleInput());
        this.input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.handleInput();
        });
    }

    addOutput(text, className = 'story-text') {
        const div = document.createElement('div');
        div.className = className;
        div.innerHTML = text.replace(/\n/g, '<br>');
        this.output.appendChild(div);
        this.output.scrollTop = this.output.scrollHeight;
    }

    async startGame() {
        try {
            const response = await fetch('/start', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            const data = await response.json();
            this.addOutput(data.message);
        } catch (error) {
            this.addOutput('Error starting game. Please refresh the page.', 'game-over');
        }
    }

    async handleInput() {
        const userChoice = this.input.value.trim();
        if (!userChoice) return;

        this.addOutput(`> ${this.input.value}`);
        const inputValue = this.input.value;
        this.input.value = '';

        try {
            const response = await fetch('/choice', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ choice: userChoice })
            });

            const data = await response.json();
            
            if (data.victory) {
                this.addOutput(data.message, 'victory');
                this.endGame();
            } else if (data.game_over) {
                this.addOutput(data.message, 'game-over');
                this.endGame();
            } else if (data.success) {
                this.addOutput(data.message);
            } else {
                this.addOutput(data.message, 'choice-text');
            }
        } catch (error) {
            this.addOutput('Error processing choice. Please try again.', 'game-over');
        }
    }

    endGame() {
        this.inputSection.style.display = 'none';
        const restartBtn = document.createElement('button');
        restartBtn.className = 'restart-btn';
        restartBtn.textContent = '🔄 Play Again';
        restartBtn.addEventListener('click', () => this.restart());
        this.output.appendChild(restartBtn);
    }

    restart() {
        this.output.innerHTML = '';
        this.inputSection.style.display = 'flex';
        this.startGame();
    }
}

// Start the game when page loads
window.addEventListener('DOMContentLoaded', () => {
    new HauntedMansionFlaskGame();
});