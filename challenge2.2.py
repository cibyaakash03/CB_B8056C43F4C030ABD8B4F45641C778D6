#
class player:
  def play(Self):
     print("The player is playing cricket")
    
    class Batsman(player):
      def play(self):
        print("The bowler is bowling")
# Create objects of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

# Call the play()method for each object
batsman.play()
bowler.play()

