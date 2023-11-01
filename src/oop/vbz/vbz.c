#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NAME_BUF 1024

// Struct defs for Stop & Line
typedef struct Vec {
    void **data;
    size_t size;
} Vec;
typedef struct Stop {
    char name[NAME_BUF];
    Vec lines;
} Stop;
typedef struct Line {
    char name[NAME_BUF];
    Vec stops;
    void (*addStop)(struct Line *line, struct Stop *stop);
} Line;

// Initializer funcs
void initVec(Vec *self) {
    self->data = NULL;
    self->size = 0;
}
void initLine(Line *self, const char *name) {
    strncpy(self->name, name, NAME_BUF-1);
    initVec(&self->stops);
    self->addStop = NULL;
}
void initStop(Stop *self, const char *name) {
    strncpy(self->name, name, NAME_BUF-1);
    initVec(&self->lines);
}
// vector push func
void push(Vec *self, void *elem) {
    self->data = realloc(self->data, self->size+1 * sizeof(void*));
    self->data[self->size++] = elem;
}

// Add stop func
void addStop(Line *self, Stop *stop) {
    push(&self->stops, stop);
    push(&stop->lines, self);
}

int main() {
    Stop a;
    Stop b;
    Line line1;
    Line line2;

    initStop(&a, "Eichtalboden");
    initStop(&b, "Baden");
    initLine(&line1, "line1");
    initLine(&line2, "line2");

    // Set the function pointers
    line1.addStop = addStop;
    line2.addStop = addStop;

    line1.addStop(&line1, &a);
    line1.addStop(&line1, &b);
    line2.addStop(&line2, &a);
    line2.addStop(&line2, &b);

    printf("Lines in A:\n");
    for (size_t i = 0; i < a.lines.size; i++) {
        Line *line = (Line *)a.lines.data[i];
        printf("%s\n", line->name);
    }

    return EXIT_SUCCESS;
}
