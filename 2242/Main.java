
/*
 * Huaauhahhuahau
 * https://www.beecrowd.com.br/judge/en/problems/view/2242
 */

import java.io.IOException;
import java.util.ArrayList;
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

    static char[] vowles = new char[] { 'a', 'e', 'i', 'o', 'u' };

    public static Boolean isVowle(char c) {
        for (int i = 0; i < vowles.length; i++) {
            if (c == vowles[i]) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        String phrase = ReadLine();
        char[] chars = phrase.toCharArray();

        List<String> funny_sequences = new ArrayList<String>();

        for (int i = 0; i < chars.length; i++) {
            if (isVowle(chars[i])) {
                funny_sequences.add(String.valueOf(chars[i]));
            }
        }

        String funny_sequence_rtl = "";
        String funny_sequence_ltr = "";

        for (int i = 0; i < funny_sequences.size(); i++) {
            funny_sequence_ltr += funny_sequences.get(i);
        }

        for (int i = funny_sequences.size() - 1; i >= 0; i--) {
            funny_sequence_rtl += funny_sequences.get(i);
        }

        if (funny_sequence_rtl.equals(funny_sequence_ltr)) {
            System.out.println("S");
        } else {
            System.out.println("N");
        }
    }
}
