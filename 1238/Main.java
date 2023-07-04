import java.io.IOException;

// Combiner
// https://www.beecrowd.com.br/judge/en/problems/view/1238
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

        int counter = 0;

        while (counter < rounds) {
            String two_words;
            String[] split_words = {};

            // Get Phrase and plit it
            two_words = ReadLine();
            split_words = two_words.split(" ");

            // Get the total length of the words
            int combined_length = 0;
            int temp_counter = 0;
            while (temp_counter < split_words.length) {
                int word_length = split_words[temp_counter].length();
                combined_length += word_length;
                temp_counter++;
            }
            //

            // combine the two words
            int char_counter = 0;
            String word_1 = split_words[0];
            String word_2 = split_words[1];
            String combined_word = "";
            while (char_counter < combined_length) {

                String char_from_word_1 = "";
                String char_from_word_2 = "";

                if (char_counter < word_1.length()) {
                    char_from_word_1 = word_1.substring(char_counter, char_counter + 1);
                }

                if (char_counter < word_2.length()) {
                    char_from_word_2 = word_2.substring(char_counter, char_counter + 1);
                }

                combined_word = combined_word + char_from_word_1 + char_from_word_2;

                char_counter++;
            }
            //

            System.out.println(combined_word);

            counter = counter + 1;
        }
    }

}