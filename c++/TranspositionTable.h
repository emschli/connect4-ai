#include<vector>

class TranspositionTable {
private:
    struct Entry {
        long key;
        unsigned char value;
    };

    std::vector<Entry> table;

public:
    TranspositionTable(unsigned int size);
    void reset();
    void put(long key, unsigned char value);
    unsigned char get(long key);
    unsigned int index(long key);
};