BEGIN
    DECLARE InputFile geraldineFile
    DECLARE InputFile gerardFile
    DECLARE OutputFile mergedFile

    OPEN geraldineFile FOR READING "Geraldines Businesses.csv"
    OPEN gerardFile FOR READING "Geralds Businesses.csv"
    OPEN mergedFile FOR WRITING "MergedBusinesses.csv"

    DECLARE uniqueCustomers AS List

    // Read first record from Geraldine's file
    WHILE NOT EOF(geraldineFile) DO
        RECORD geraldineRecord = READ FROM geraldineFile
        IF NOT EXISTS(geraldineRecord.customerNumber IN uniqueCustomers) THEN
            ADD geraldineRecord TO uniqueCustomers
        END IF
    END WHILE

    // Read first record from Gerard's file
    WHILE NOT EOF(gerardFile) DO
        RECORD gerardRecord = READ FROM gerardFile
        IF NOT EXISTS(gerardRecord.customerNumber IN uniqueCustomers) THEN
            ADD gerardRecord TO uniqueCustomers
        END IF
    END WHILE

    // Write unique records to merged file
    FOR EACH customer IN uniqueCustomers DO
        WRITE customer TO mergedFile
    END FOR

    CLOSE geraldineFile
    CLOSE gerardFile
    CLOSE mergedFile
END
