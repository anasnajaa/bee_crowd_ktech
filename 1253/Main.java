
/*
 * Huaauhahhuahau
 * https://www.beecrowd.com.br/judge/en/problems/view/1253
 */

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static String ReadLine() throws IOException {
        String accumulator = "";
        char c;
        while ((c = (char) System.in.read()) != '\n') {
            accumulator += c;
        }

        return accumulator;
    }

    static List<String> ALPHA = Arrays.asList(
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z");

    public static void main(String[] args) throws IOException {
        int rounds = Integer.parseInt(ReadLine());

        for (int m = 0; m < rounds; m++) {

            String coded_sentence = ReadLine();
            int shift = Integer.parseInt(ReadLine());

            List<String> SHIFTED_ALPHA = new ArrayList<String>();

            for (int i = 0; i < ALPHA.size(); i++) {
                int new_index = i + shift;

                if (new_index >= ALPHA.size()) {
                    new_index = new_index - ALPHA.size();
                }

                SHIFTED_ALPHA.add(ALPHA.get(new_index));
            }

            char[] coded_sentence_chars = coded_sentence.toCharArray();

            String decoded_sentence = "";
            for (int i = 0; i < coded_sentence_chars.length; i++) {
                int index = SHIFTED_ALPHA.indexOf(String.valueOf(coded_sentence_chars[i]));
                decoded_sentence += ALPHA.get(index);
            }

            System.out.println(decoded_sentence);
        }
    }
}
