# pārveido masīvu par min-heap (katra mezgla vērtība ir mazāka vai vienāda par tā zaru vērtībām)
def make_heap(n_elements, arr):
  swaps = []
  
  def heapify(i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # jāsaprot vai konkrētā mezgla zaru vērtība ir mazāka par paša vērtību
    # t.i., no visiem trim mezgliem atrodam mazākās vērtības indeksu
    if left <= n_elements - 1 and arr[left] < arr[smallest]:
      smallest = left
    if right <= n_elements - 1 and arr[right] < arr[smallest]:
      smallest = right

    # ja atradām indeksu, kurā ir mazāka vērtība par šobrīdējo mezglu 'i',
    # tad samainām to vietām ar 'i' vērtību
    if i != smallest:
      arr[i], arr[smallest] = arr[smallest], arr[i]

      # atceramies, kādos indeksos mainījām elementus
      swaps.append((i,smallest))

      # tā kā atradām jaunu mazāko elementu, skaidrs, ka bija iespējams veikt izmaiņas heap struktūrā (t.i., neesam sasnieguši galotni)
      # tādēļ mēģinām meklēt no mazākā indeksa uz leju
      heapify(smallest)
  
  # mums nevajag iterēt pāri katram elementam, jo tad mēs pārbaudītu vienus un tos pašus mezglus vairākas reizes
  for i in range(n_elements // 2 - 1, -1, -1):
    heapify(i)
    
  # print(arr)

  total_swaps = len(swaps)
  assert total_swaps < 4 * n_elements

  pretty_indeces_separated_by_newlines = "\n".join([ f"{i}, {j}" for i, j in swaps ])
  print(total_swaps, pretty_indeces_separated_by_newlines, sep="\n")
 
arr = [5,4,3,2,1]
n = len(arr)
make_heap(n, arr)

