public class CodeWordChecker {

    private final int minLength;
    private final int maxLength;
    private final String forbidden;

    public CodeWordChecker(int minLength, int maxLength, String forbidden) {
        if (minLength < 0 || maxLength < minLength) {
            throw new IllegalArgumentException("Invalid length bounds");
        }
        if (forbidden == null) {
            throw new IllegalArgumentException("Forbidden string cannot be null");
        }

        this.minLength = minLength;
        this.maxLength = maxLength;
        this.forbidden = forbidden;
    }

    public CodeWordChecker(String forbidden) {
        this(6, 20, forbidden);
    }

    public boolean isValid(String word) {
        if (word == null) {
            return false;
        }

        int length = word.length();
        return length >= minLength
            && length <= maxLength
            && !word.contains(forbidden);
    }
}