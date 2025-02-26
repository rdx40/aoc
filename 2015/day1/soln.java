import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class soln {
    public static void main(String[] args) {
        String fileName = "input.txt";
        String input = "";
        
        // Read the contents of the file into the input string
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            StringBuilder sb = new StringBuilder();
            String line;
            
            while ((line = reader.readLine()) != null) {
                sb.append(line);
            }
            
            input = sb.toString();
        } catch (IOException e) {
            e.printStackTrace(); 
        }

        int floor = 0;
        for (char ch : input.toCharArray()) {
            if (ch == '(') {
                floor++;
            } else if (ch == ')') {
                floor--;
            }
        }
        System.out.println("Part 1: Final floor: " + floor);
        
        int position = 0;
        floor = 0;
        for (char ch : input.toCharArray()) {
            position++;
            if (ch == '(') {
                floor++;
            } else if (ch == ')') {
                floor--;
            }
            if (floor == -1) {
                System.out.println("Part 2: First basement position: " + position);
                break;
            }
        }
    }
}

