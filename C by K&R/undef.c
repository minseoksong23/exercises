// ex6-5

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASHSIZE 101

struct nlist { /* table entry: */
    struct nlist *next; /* next entry in chain */
    char *name;         /* defined name */
    char *defn;         /* replacement text */
};

static struct nlist *hashtab[HASHSIZE]; /* pointer table */

/* hash: form hash value for string s */
unsigned hash(char *s)
{
    unsigned hashval;

    for (hashval = 0; *s != '\0'; s++)
        hashval = *s + 31 * hashval;
    return hashval % HASHSIZE;
}

/* lookup: look for s in hashtab */
struct nlist *lookup(char *s)
{
    struct nlist *np;

    for (np = hashtab[hash(s)]; np != NULL; np = np->next)
        if (strcmp(s, np->name) == 0)
            return np; /* found */
    return NULL; /* not found */
}

/* install: put (name, defn) in hashtab */
struct nlist *install(char *name, char *defn)
{
    struct nlist *np;
    unsigned hashval;

    if ((np = lookup(name)) == NULL) { /* not found */
        np = (struct nlist *) malloc(sizeof(*np));
        if (np == NULL || (np->name = strdup(name)) == NULL)
            return NULL;
        hashval = hash(name);
        np->next = hashtab[hashval];
        hashtab[hashval] = np;
    } else { /* already there */
        free((void *) np->defn); /* free previous defn */
    }
    if ((np->defn = strdup(defn)) == NULL)
        return NULL;
    return np;
}

/* strdup: make a duplicate of s */
char *strdup(char *s)
{
    char *p;

    p = (char *) malloc(strlen(s) + 1); /* +1 for '\0' */
    if (p != NULL)
        strcpy(p, s);
    return p;
}

void undef(char *name) {
    struct nlist *current, *prev = NULL;
    unsigned hashval = hash(name);

    /* Find the node and keep track of the previous node */
    for (current = hashtab[hashval]; current != NULL; prev = current, current = current->next) {
        if (strcmp(name, current->name) == 0) {
            break;
        }
    }

    if (current == NULL) {
        return; /* Not found */
    }

    /* Unlink the node from the list */
    if (prev == NULL) {
        /* The node to delete is the first node in the list */
        hashtab[hashval] = current->next;
    } else {
        /* The node to delete is in the middle or at the end of the list */
        prev->next = current->next;
    }

    /* Free the node */
    free(current->name);
    free(current->defn);
    free(current);
}
