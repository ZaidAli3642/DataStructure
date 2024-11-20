public class Array {
    private int[] items;
    private int count = 0;
    private int size;

    public Array(int length) {
        items = new int[length];
        size = length;
    }

    public void insert(int value) {
        resizeArray();
        items[count++] = value;
    }

    private void resizeArray(){
        if(count != size - 1) return;

        size = size * 2;
        int[] newItems = new int[size];
        for (int i = 0; i < count; i++) {
            newItems[i] = items[i];
        }
        items = newItems;
    }

    public void removeAt(int index){
        if(index < 0 || index > count) return;

        for(int i = index; i < count; i++){
            items[i] = items[i + 1];
        }
        --count;
    }

    public int indexOf(int value){
        for(int i = 0; i < count; i++){
            if(items[i] == value) return i;
        }

        return -1;
    }

    // RUNTIME COMPLEXITY: O(n)
    public int max(){
        // if items have no value then return -1
        if (count == 0) return -1;

        // if item has only 1 value;
        if(count == 1) return items[count];

        // starting from 2nd index
        int max = items[0];
        for(int i = 1; i < count; i++) {
            if(items[i] > max){
                max = items[i];
            }
        }

        return max;
    }

    public Array intersect(int[] others) {
        var intersection = new Array(count);

        for (int other : others)
            if (indexOf(other) >= 0)
                intersection.insert(other);

        return intersection;
    }

    public void reverse(){
        int[] newArray = new int[count];
        for (int i = 0; i < count; i++) {
            newArray[i] = items[count - 1 - i];
        }

        items = newArray;
    }

    public void insertAt(int index, int value){
        resizeArray();
        for (int i = count; i >= 0; i--) {
            items[i + 1] = items[i];

            if (i == index) break;
        }

        items[index] = value;
        ++count;
    }

    public void print(){
        for(int i = 0; i < count; i++){
            System.out.println(items[i]);
        }
    }
}
