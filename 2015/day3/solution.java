import java.io.*;
import java.util.*;

public class solution{

    public static int cntHouses(String moves) {
        Set<String> visited = new HashSet<>();
        int x = 0, y = 0;
        visited.add(x + "," + y); 

        for (char move : moves.toCharArray()) {
            switch (move) {
                case '^':
                    y++;
                    break;
                case 'v':
                    y--;
                    break;
                case '>':
                    x++;
                    break;
                case '<':
                    x--;
                    break;
            }
            visited.add(x + "," + y); // Adding the new position
        }

        return visited.size();
    }

    public static int cntHousesTwo(String moves) {
        Set<String> visited = new HashSet<>();
        int a = 0, b = 0; 
        int c = 0, d = 0; 
        visited.add(a + "," + b);

        for (int i = 0; i < moves.length(); i++) {
            char move = moves.charAt(i);
            if (i % 2 == 0) {
                switch (move) {
                    case '^':
                        b++;
                        break;
                    case 'v':
                        b--;
                        break;
                    case '>':
                        a++;
                        break;
                    case '<':
                        a--;
                        break;
                }
                visited.add(a + "," + b);
            } else {
                switch (move) {
                    case '^':
                        d++;
                        break;
                    case 'v':
                        d--;
                        break;
                    case '>':
                        c++;
                        break;
                    case '<':
                        c--;
                        break;
                }
                visited.add(c + "," + d); 
            }
        }

        return visited.size();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        String moves = reader.readLine().trim();
        reader.close();

        System.out.println("Part 1: " + cntHouses(moves));
        System.out.println("Part 2: " + cntHousesTwo(moves));
    }
}

