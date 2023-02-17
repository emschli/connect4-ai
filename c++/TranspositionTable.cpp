#include "TranspositionTable.h"
#include <string.h>

TranspositionTable::TranspositionTable(unsigned int size) : table(size) {}

void TranspositionTable::reset() {
    memset(&table[0], 0, table.size() * sizeof(Entry));
}

void TranspositionTable::put(long key, unsigned char value) {
    unsigned int i = index(key);
    table[i].key = key;
    table[i].value = value;
}

unsigned char TranspositionTable::get(long key) {
    unsigned int i = index(key);

    if (table[i].key == key) {
        return table[i].value;
    } else {
        return 0;
    }

}

unsigned int TranspositionTable::index(long key) {
    return key % table.size();
}