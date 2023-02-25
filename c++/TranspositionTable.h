#include<vector>

class TranspositionTable {
private:
    struct Entry {
        long long key;
        unsigned char value;
    };

    std::vector<Entry> table;

public:
    TranspositionTable(unsigned int size);
    void reset();
    void put(long long key, unsigned char value);
    unsigned char get(long long key);
    unsigned int index(long long key);
};