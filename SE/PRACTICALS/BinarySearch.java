import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.Test;

public class BinarySearch {
    int binarySearch(int arr[], int x) {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (arr[m] == x)
                return m;
            if (arr[m] < x)
                l = m + 1;
            else
                r = m - 1;
        }
        return -1;
    }

    public static void main(String args[]) {
        // Main
    }

    int UNSUCCESSFUL = -1;
    int[] arr = { 1, 2, 4, 7, 8, 12, 15, 19, 24, 50, 69, 80, 100 };

    @Test
    public void testShouldReturnUnsuccessfulOnEmptyArray() {
        assertEquals(UNSUCCESSFUL, binarySearch(new int[] {}, 0));
    }

    @Test
    public void testShouldReturnUnsuccessfulOnLeftBound() {
        assertEquals(UNSUCCESSFUL, binarySearch(arr, 0));
    }

    @Test
    public void testShouldReturnUnsuccessfulOnRightBound() {
        assertEquals(UNSUCCESSFUL, binarySearch(arr, 101));
    }

    @Test
    public void testShouldReturnSuccessfulOnLeftBound() {
        assertEquals(0, binarySearch(arr, 1));
    }

    @Test
    public void testShouldReturnSuccessfulOnRightBound() {
        assertEquals(12, binarySearch(arr, 100));
    }

    @Test
    public void testShouldReturnSuccessfulOnMid() {
        assertEquals(7, binarySearch(arr, 19));
    }

    @Test
    public void testShouldReturnSuccessfulOnMidGreaterThanGivenNumber() {
        assertEquals(5, binarySearch(arr, 12));
    }

    @Test
    public void testShouldReturnSuccessfulOnMidLesserThanGivenNumber() {
        assertEquals(10, binarySearch(arr, 69));
    }
}
