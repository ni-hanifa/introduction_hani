int main() {
    int c;
    scanf ("%d", &c);
    int a;
    for( a = 1; c > a; a++){
        c = c - a;
    }
    printf("%d", a);
}