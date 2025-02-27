import java.io.*;
import java.util.*;

public class soln{

    public static int[] calculateWrappingPaperAndRibbon(List<String> dimensions) {
        int totalPaper = 0;
        int totalRibbon = 0;

        for (String dim : dimensions) {
            String[] dims = dim.split("x");
            int l = Integer.parseInt(dims[0]);
            int w = Integer.parseInt(dims[1]);
            int h = Integer.parseInt(dims[2]);

            int surfaceArea = 2 * (l * w + w * h + h * l);
            int smallestSide = Math.min(l * w, Math.min(w * h, h * l));
            int totalPaperForPresent = surfaceArea + smallestSide;
            totalPaper += totalPaperForPresent;

            int smallestPerimeter = 2 * (Math.min(l + w, Math.min(w + h, h + l)));
            int volume = l * w * h;
            int totalRibbonForPresent = smallestPerimeter + volume;
            totalRibbon += totalRibbonForPresent;
        }

        return new int[]{totalPaper, totalRibbon};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        List<String> dimensions = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null) {
            dimensions.add(line);
        }
        br.close();

        int[] results = calculateWrappingPaperAndRibbon(dimensions);
        int totalPaper = results[0];
        int totalRibbon = results[1];

        System.out.println(totalPaper); 
	System.out.println(totalRibbon);
    }
}
