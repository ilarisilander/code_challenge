using System;


namespace WordCounter
{
    public class InputArgument
    {
        public static bool IsValidArgument(string[] args)
        {
            try
            {   
                if(args.Length < 1)
                {
                    throw new ArgumentException($"Run program with a path as argument");
                }
                if(args.Length > 1)
                {
                    throw new ArgumentException($"Program only takes one path as argument");
                }
                if(!File.Exists(args[0]))
                {
                    throw new ArgumentException($"{args[0]} path does not contain a file");
                }
                if(!IsValidExtension(args[0]))
                {
                    throw new ArgumentException($"{args[0]} has the wrong extension");
                }

                if(!FileHasNoSpaces(args[0]))
                {
                    throw new ArgumentException($"{args[0]} has spaces in file name");
                }

                return true;
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error: {e.Message}");
                return false;
            }
        }

        static bool IsValidExtension(string filePath)
        {
            return filePath.EndsWith(".txt", StringComparison.OrdinalIgnoreCase);
        }

        static bool FileHasNoSpaces(string filePath)
        {
            string fileName = Path.GetFileNameWithoutExtension(filePath);
            foreach(char character in fileName)
            {
                if(char.IsWhiteSpace(character))
                {
                    return false;
                }
            }
            return true;
        }
    }
}