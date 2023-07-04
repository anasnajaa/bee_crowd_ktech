import java.io.IOException;

// One-Two-Three
// https://www.beecrowd.com.br/judge/en/problems/view/1332
public class Main {

    public static String ReadLine() throws IOException {
        String accumulator = "";
        char c;
        while ((c = (char) System.in.read()) != '\n') {
            accumulator += c;
        }

        return accumulator;
    }

    public static String[] get_words_with_same_length(String[] words_list, String word) {
        int words_same_length_count = 0;

        int user_input_length = word.length();

        // get the count
        for (int i = 0; i < words_list.length; i++) {
            if (words_list[i].length() == user_input_length) {
                words_same_length_count++;
            }
        }

        // create the array
        String[] words_same_length = new String[words_same_length_count];
        int counter = 0;
        for (int i = 0; i < words_list.length; i++) {
            if (words_list[i].length() == user_input_length) {
                words_same_length[counter] = words_list[i];
                counter++;
            }
        }

        return words_same_length;
    }

    public static void main(String[] args) throws IOException {
        String[] auto_correct_words = new String[] { "one", "two", "three" };

        String input_rounds = ReadLine();
        int rounds = Integer.parseInt(input_rounds);

        String[] input_word_typo_array = new String[rounds];

        for (int i = 0; i < input_word_typo_array.length; i++) {
            input_word_typo_array[i] = ReadLine();
        }

        for (int m = 0; m < input_word_typo_array.length; m++) {
            String input_word_typo = input_word_typo_array[m];

            // find words with the same length
            String[] auto_correct_words_same_length = get_words_with_same_length(auto_correct_words, input_word_typo);

            String correct_word_found = "";

            // guess words of typo
            for (int i = 0; i < auto_correct_words_same_length.length; i++) {
                String auto_correct_word = auto_correct_words_same_length[i];

                if (input_word_typo.equals(auto_correct_word)) {
                    // exact match, get out
                    correct_word_found = auto_correct_word;
                    break;
                }

                char[] typo_chars = input_word_typo.toCharArray();
                char[] word_chars = auto_correct_word.toCharArray();

                int typos_counter = 0;
                for (int k = 0; k < typo_chars.length; k++) {
                    if (word_chars[k] != typo_chars[k]) {
                        typos_counter++;
                    }
                }

                if (typos_counter == 1) {
                    // one wrong char, word found, get out
                    correct_word_found = auto_correct_word;
                    break;
                }
            }

            if (correct_word_found == "one") {
                System.out.println("1");
            } else if (correct_word_found == "two") {
                System.out.println("2");
            } else if (correct_word_found == "three") {
                System.out.println("3");
            }
        }
    }
}
