package Konkurens.gy.gy1;

public class Triple<T, U, V> {
    private T first;
    private U second;
    private V third;

    @Override
    public boolean equals(Object that) {
        if (that instanceof Triple<?, ?, ?>) {
            Triple<?, ?, ?> thatTriple = (Triple<?, ?, ?>) that;
        }
        return false;

    }

}
