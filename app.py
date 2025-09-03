from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

class HauntedMansionGame:
    def __init__(self):
        self.reset_game()
    
    def reset_game(self):
        self.state = 'room_choice'
        self.story = []
    
    def process_choice(self, choice):
        choice = choice.lower().strip()
        
        if self.state == 'room_choice':
            return self.handle_room_choice(choice)
        elif self.state == 'pitbull_choice':
            return self.handle_pitbull_choice(choice)
        elif self.state == 'stair_choice':
            return self.handle_stair_choice(choice)
        elif self.state == 'door_choice':
            return self.handle_door_choice(choice)
        elif self.state == 'passage_choice':
            return self.handle_passage_choice(choice)
        elif self.state == 'vase_choice':
            return self.handle_vase_choice(choice)
        elif self.state == 'attic_choice':
            return self.handle_attic_choice(choice)
        elif self.state == 'code_choice':
            return self.handle_code_choice(choice)
    
    def handle_room_choice(self, choice):
        if choice == "living room":
            self.state = 'pitbull_choice'
            return {
                'success': True,
                'message': "\nYou enter the living room.\nAs you walk in, you see a sleeping pitbull 🐕 guarding some gold jewelry.\nDo you want to steal the jewelry from the pitbull? (yes/no)",
                'game_over': False
            }
        elif choice == "dining room":
            self.state = 'vase_choice'
            return {
                'success': True,
                'message': "\nYou chose to go into the dining room.\nAs you walk in, you see a shiny vase on the table.\nDo you want to open the vase? (yes/no)",
                'game_over': False
            }
        else:
            return {
                'success': False,
                'message': "Invalid choice. Please enter 'living room' or 'dining room'.",
                'game_over': False
            }
    
    def handle_pitbull_choice(self, choice):
        if choice == "yes":
            return {
                'success': True,
                'message': "You attempt to steal the jewelry, but the pitbull wakes up and attacks you!\n💀 You are now dead. Game Over.",
                'game_over': True
            }
        elif choice == "no":
            self.state = 'stair_choice'
            return {
                'success': True,
                'message': "You decide not to disturb the pitbull.\nAs you turn around, you notice a hidden staircase behind an old bookshelf!\nDo you want to go down the hidden staircase? (yes/no)",
                'game_over': False
            }
        else:
            return {
                'success': False,
                'message': "Invalid choice. Please enter 'yes' or 'no'.",
                'game_over': False
            }
    
    def handle_stair_choice(self, choice):
        if choice == "yes":
            self.state = 'door_choice'
            return {
                'success': True,
                'message': "\nYou carefully walk down the creaky stairs into a dark basement.\nYou find three doors labeled A, B, and C. One of them leads to the treasure, the others lead to traps!\nWhich door do you choose? (A/B/C)",
                'game_over': False
            }
        else:
            return {
                'success': True,
                'message': "You leave the living room safely without exploring further.",
                'game_over': True
            }
    
    def handle_door_choice(self, choice):
        if choice == "a":
            return {
                'success': True,
                'message': "You open the door and find a room full of bats 🦇 that attack you!\n💀 You are now dead. Game Over.",
                'game_over': True
            }
        elif choice == "b":
            self.state = 'passage_choice'
            return {
                'success': True,
                'message': "You open the door and step into a room filled with ancient paintings and dusty chests.\nInside one chest, you discover a mysterious golden key 🔑.\nA secret passage opens behind the chest!\nDo you want to enter the secret passage? (yes/no)",
                'game_over': False
            }
        elif choice == "c":
            return {
                'success': True,
                'message': "You open the door, but the floor collapses and you fall into a spike pit!\n💀 You are now dead. Game Over.",
                'game_over': True
            }
        else:
            return {
                'success': False,
                'message': "Invalid choice. Please enter A, B, or C.",
                'game_over': False
            }
    
    def handle_passage_choice(self, choice):
        if choice == "yes":
            return {
                'success': True,
                'message': "\nYou crawl through the passage and arrive at a giant locked door.\nYou use the golden key 🔑, and the door creaks open...\n🌟 Inside, you find a hidden treasure chamber filled with glittering diamonds 💎!\n🎉 Congratulations! You found the hidden treasure and became the richest person alive!",
                'game_over': True,
                'victory': True
            }
        else:
            return {
                'success': True,
                'message': "You decide not to enter the passage and leave the mansion safely.",
                'game_over': True
            }
    
    def handle_vase_choice(self, choice):
        if choice == "yes":
            self.state = 'attic_choice'
            return {
                'success': True,
                'message': "You open the vase and find a pile of bones! 🦴\nBut inside, you also notice a tiny map hidden beneath the bones.\nThe map shows a secret attic where the diamonds might be hidden!\nDo you want to follow the map to the attic? (yes/no)",
                'game_over': False
            }
        elif choice == "no":
            return {
                'success': True,
                'message': "You decide not to open the shiny vase.\nAs you turn to leave, you hear a cracking sound coming from the corner.\nA dark figure with glowing red eyes launches at you, knocking you unconscious.\nYou wake up in your bed. It was all a dream... or was it?",
                'game_over': True
            }
        else:
            return {
                'success': False,
                'message': "Invalid choice. Please enter 'yes' or 'no'.",
                'game_over': False
            }
    
    def handle_attic_choice(self, choice):
        if choice == "yes":
            self.state = 'code_choice'
            return {
                'success': True,
                'message': "\nYou climb up a narrow staircase into the dusty attic.\nYou find an old chest with a combination lock.\nThe map says: 'The code is the sum of 12 and 23.' What code do you enter?",
                'game_over': False
            }
        else:
            return {
                'success': True,
                'message': "You ignore the map and leave the dining room safely.",
                'game_over': True
            }
    
    def handle_code_choice(self, choice):
        if choice == "35":
            return {
                'success': True,
                'message': "✅ Correct code! The chest creaks open...\n🌟 Inside, you find the treasure of diamonds 💎!\n🎉 Congratulations! You won the game!",
                'game_over': True,
                'victory': True
            }
        else:
            return {
                'success': True,
                'message': "❌ Wrong code! A hidden trapdoor opens beneath you and you fall into darkness...\n💀 Game Over.",
                'game_over': True
            }

# Global game instance
game = HauntedMansionGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    game.reset_game()
    return jsonify({
        'message': "🏚️ Welcome to the Haunted Mansion!\nYou are a distant family member of a rich millionaire who has just passed away, leaving this mysterious mansion to you.\nRumors say there's a hidden treasure of diamonds 💎 somewhere inside...\nYou gather your courage and step inside the creaky old house.\nDo you want to enter the living room or the dining room?"
    })

@app.route('/choice', methods=['POST'])
def make_choice():
    data = request.get_json()
    choice = data.get('choice', '')
    result = game.process_choice(choice)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)