/*
Hidden Message
https://www.beecrowd.com.br/judge/en/problems/view/1272

sample inputs:
compete·online·design·event·rating
compete online design event rating
··u····r·i··o····n·l··i····n··e···
  u    r i  o    n l  i    n  e   
.
 
round··elimination·during··onsite··contest
round  elimination during  onsite  contest
------------------------------------------
sample outputs:
coder
urionline

redoc
 */

import java.io.IOException;

public class Main {
    public static String ReadLine() throws IOException {
        String accumulator = "";
        char c;
        while ((c = (char) System.in.read()) != '\n') {
            accumulator += c;
        }

        return accumulator;
    }

    public static void main(String[] args) throws IOException {

        String rounds_string = ReadLine();

        int rounds = Integer.parseInt(rounds_string);

        for (int m = 0; m < rounds; m++) {
            String hidden_message = "";
            String phrase = ReadLine();
            phrase = phrase.trim();

            String[] words = phrase.split(" ");

            for (int i = 0; i < words.length; i++) {
                String word = words[i];

                if (word.length() > 0 && word != " ") {
                    char first_char = word.charAt(0);
                    hidden_message += first_char;
                }
            }

            System.out.println(hidden_message);
        }

    }
}