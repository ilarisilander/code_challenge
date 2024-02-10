using System;
using System.IO;


namespace WordCounter
{
    public class TextFile
    {
        private readonly string filePath;
        private readonly string fileName;

        public TextFile(string filePath)
        {
            FilePath = filePath;
            FileName = Path.GetFileNameWithoutExtension(filePath);
        }

        public string[] FileContentToArray()
        {
            char[] separators = {' ', '\n', '\r', '\t'};
            string contentString = File.ReadAllText(FilePath, System.Text.Encoding.UTF8);
            string[] words = contentString.Split(separators, StringSplitOptions.RemoveEmptyEntries);

            return words;
        }

        public int CountWordsInArray(string[] words)
        {
            int counter = 0;
            for(int i = 0; i < words.Length; i++)
            {
                if(words[i].Contains(FileName, StringComparison.OrdinalIgnoreCase))
                {
                    counter++;
                }
            }
            return counter;
        }

        public void PrintWordCount(int counter)
        {
            Console.WriteLine($"The word {FileName} appeared {counter} times");
        }

        public string FileName { get; }
        public string FilePath { get; }
    }
}